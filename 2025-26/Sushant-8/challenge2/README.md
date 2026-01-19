I did this problem by separating it into 3 parts:
1) LOGs: read all the logs and only identify imp messages like errors, failures or exceptions.. And after that generate a summary report
2)Port clash detetction: to identify the container responsible for each clash
Duplicate ports were detected by extracting host mappings and by checking repeated values using sort and uniq.

3)Auto Recovery: after a clash is detected, restart the affected container and then log the recovery result in the report




## Simulating a Port Clash

To test the script:

1. Run one container on port 8080:

   docker run -d -p 8080:80 nginx

2. Try running another container on the same port:

   docker run -d -p 8080:80 nginx

3. Execute the script:

   bash check.sh

The script should detect the conflict and attempt recovery automatically.

---

## Output Files

- **summary_report.txt** : structured report of log analysis and recovery actions.
- **sample_output.txt**:example terminal output from a real run.
- **check.sh** : main script


the difficulty i faced was I missed a lot of error messages because I was reading logs without `2>&1`. Afterwards, I realized that stderr and stdout needed to be combined.

