import json
import time
import tracemalloc
from pathlib import Path

from parsers.resume_text_extractor import clean_resume_text


INPUT_FILE = "data/extracted_resumes/sample_resume.txt"
OUTPUT_FILE = "data/performance_outputs/day18_optimized_result.json"
ITERATIONS = 1000


def run_optimized_benchmark():
    resume_text = Path(INPUT_FILE).read_text(encoding="utf-8", errors="ignore")

    tracemalloc.start()
    start_time = time.perf_counter()

    cleaned_text = ""

    for _ in range(ITERATIONS):
        cleaned_text = clean_resume_text(resume_text)

    end_time = time.perf_counter()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    total_time_ms = round((end_time - start_time) * 1000, 2)
    average_time_ms = round(total_time_ms / ITERATIONS, 4)

    result = {
        "test_name": "Day 18 Optimized Resume Cleaning Benchmark",
        "input_file": INPUT_FILE,
        "iterations": ITERATIONS,
        "input_characters": len(resume_text),
        "output_characters": len(cleaned_text),
        "total_time_ms": total_time_ms,
        "average_time_per_run_ms": average_time_ms,
        "peak_memory_kb": round(peak_memory / 1024, 2),
        "status": "optimized_result_recorded"
    }

    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

    Path(OUTPUT_FILE).write_text(
        json.dumps(result, indent=2),
        encoding="utf-8"
    )

    print("Optimized benchmark completed.")
    print(f"Average time per run: {average_time_ms} ms")
    print(f"Peak memory usage: {result['peak_memory_kb']} KB")
    print(f"Result saved at: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_optimized_benchmark()
