import os
import json

def summarize_question_counts(input_dir, output_file):
    summary = {"documents": [], "total_questions": 0}
    
    # Loop through all files in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(input_dir, filename)
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
                
                # Only include if "question_count" exists
                if "question_count" in data:
                    doc_summary = {
                        "document": filename,
                        "question_count": data["question_count"]
                    }
                    summary["documents"].append(doc_summary)
                    summary["total_questions"] += data["question_count"]
            except Exception as e:
                print(f"Skipping {filename}: {e}")
    
    # Write summary JSON
    with open(output_file, "w") as f:
        json.dump(summary, f, indent=2)

if __name__ == "__main__":
    input_dir = "./reports"
    output_file = os.path.join(input_dir, "question_count_summary.json")
    summarize_question_counts(input_dir, output_file)
    print(f"Summary written to {output_file}")
