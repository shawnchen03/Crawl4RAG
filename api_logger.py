import os
import json
import time
from datetime import datetime
from typing import Dict, Any

class APILogger:
    """Logger for API calls to Jina Reader and GPT"""
    
    def __init__(self, run_dir: str):
        self.log_dir = os.path.join(run_dir, "api_logs")
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Create separate log files
        self.jina_log = os.path.join(self.log_dir, "jina_calls.jsonl")
        self.gpt_log = os.path.join(self.log_dir, "gpt_calls.jsonl")
    
    def log_jina_call(self, url: str, status: int, success: bool, error: str = None):
        """Log Jina Reader API call"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "api": "jina_reader",
            "url": url,
            "status_code": status,
            "success": success,
            "error": error,
        }
        self._append_log(self.jina_log, log_entry)
    
    def log_gpt_call(self, prompt_tokens: int, completion_tokens: int, 
                     success: bool, error: str = None, task: str = None):
        """Log GPT API call"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "api": "gpt-4o-mini",
            "task": task,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
            "estimated_cost": self._calculate_gpt_cost(prompt_tokens, completion_tokens),
            "success": success,
            "error": error
        }
        self._append_log(self.gpt_log, log_entry)
    
    def _append_log(self, log_file: str, entry: Dict[str, Any]):
        """Append entry to log file"""
        try:
            with open(log_file, 'a', encoding='utf-8') as f:
                json.dump(entry, f)
                f.write('\n')
        except Exception as e:
            print(f"Error writing to log: {str(e)}")
    
    def _calculate_gpt_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate estimated cost in USD"""
        # GPT-4 40-mini pricing: $3.00 per 1M tokens
        MODEL_NAME = "gpt-4-40-mini"
        COST_PER_1M = 3.00
        total_tokens = prompt_tokens + completion_tokens
        total_cost = (total_tokens / 1_000_000) * COST_PER_1M
        
        print(f"\n{MODEL_NAME} Cost Breakdown:")
        print(f"Total tokens: {total_tokens:,}")
        print(f"Estimated cost: ${total_cost:.4f} (${COST_PER_1M}/1M tokens)")
        
        return round(total_cost, 4)
    
    def get_summary(self) -> Dict:
        """Get summary of API usage"""
        jina_calls = self._read_logs(self.jina_log)
        gpt_calls = self._read_logs(self.gpt_log)
        
        return {
            "jina_reader": {
                "total_calls": len(jina_calls),
                "successful_calls": sum(1 for call in jina_calls if call["success"]),
                "failed_calls": sum(1 for call in jina_calls if not call["success"])
            },
            "gpt-4-40-mini": {
                "total_calls": len(gpt_calls),
                "successful_calls": sum(1 for call in gpt_calls if call["success"]),
                "total_tokens": sum(call["total_tokens"] for call in gpt_calls if call["success"]),
                "total_cost": sum(call["estimated_cost"] for call in gpt_calls if call["success"])
            }
        }
    
    def _read_logs(self, log_file: str) -> list:
        """Read all entries from a log file"""
        entries = []
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        entries.append(json.loads(line))
                    except:
                        continue
        return entries 