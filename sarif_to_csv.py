import json
import csv

def sarif_to_csv(sarif_path, csv_path):
    # Load SARIF file
    with open(sarif_path, 'r') as sarif_file:
        sarif_data = json.load(sarif_file)

    # Open CSV file for writing
    with open(csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write the CSV header
        csv_writer.writerow([
            'Tool', 'RuleId', 'Message', 'Severity', 'File', 'StartLine', 'EndLine', 
            'Branch', 'RepositoryUri', 'CommitId'
        ])

        # Extract results from SARIF data
        for run in sarif_data.get("runs", []):
            tool_name = run.get("tool", {}).get("driver", {}).get("name", "")
            branch = run.get("versionControlProvenance", [{}])[0].get("branch", "")
            repo_uri = run.get("versionControlProvenance", [{}])[0].get("repositoryUri", "")
            commit_id = run.get("versionControlProvenance", [{}])[0].get("revisionId", "")
            
            # Check if there are any results to process
            if run.get("results", []):
                for result in run["results"]:
                    rule_id = result.get("ruleId", "")
                    message = result.get("message", {}).get("text", "")
                    level = result.get("level", "")  # Severity level

                    for location in result.get("locations", []):
                        file = location.get("physicalLocation", {}).get("artifactLocation", {}).get("uri", "")
                        region = location.get("physicalLocation", {}).get("region", {})
                        start_line = region.get("startLine", "")
                        end_line = region.get("endLine", "")
                        
                        csv_writer.writerow([tool_name, rule_id, message, level, file, start_line, end_line, branch, repo_uri, commit_id])
            else:
                # If no results, write tool, branch, repo, commit details without results
                csv_writer.writerow([tool_name, '', '', '', '', '', '', branch, repo_uri, commit_id])

    print(f"SARIF data successfully converted to CSV at {csv_path}")

# Replace 'app.sarif' and 'app.csv' with your file paths
sarif_to_csv('app.sarif', 'app.csv')
