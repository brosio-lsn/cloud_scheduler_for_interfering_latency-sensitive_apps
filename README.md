# Cloud Computing Architecture - Automated Cluster Management

## Project Overview

This project was developed as part of a semester-long study at **ETH Zurich** to design, deploy, and manage cloud computing workloads using **Kubernetes** and Google Cloud. The focus of the project was on optimizing both **latency-sensitive** and **batch processing** applications in a dynamically managed cluster environment. 

Our work involved building a fully automated infrastructure using **Bash scripts** to deploy, monitor, and manage clusters in real-time. The project demonstrated significant technical skills in **cloud orchestration**, **performance optimization**, and **dynamic resource allocation** across multiple nodes and virtual machines (VMs). 

Details of our implementations, experiments, and findings are comprehensively documented in our project reports. This README highlights key aspects of our work, particularly our creative solutions in performance management and automation, which are of high interest to recruiters.

## Key Features

### Kubernetes-Based Cluster Management
- **Containerized Applications**: We deployed applications like **memcached** (latency-sensitive) and **PARSEC benchmarks** (batch workloads) inside Kubernetes-managed containers.
- **Dynamic Scaling and Scheduling**: Our solution involved scaling applications dynamically based on real-time resource consumption and performance constraints.

### Full Automation with Bash Scripting
- **Automated Cluster Creation**: Using **Kops** and **Google Cloud SDK**, we wrote custom Bash scripts to automate the setup and teardown of Kubernetes clusters. Our scripts handle every aspect of cluster initialization and resource provisioning.
- **Concurrent Command Execution**: We developed scripts to run commands concurrently across multiple VMs, significantly reducing setup time.
- **Dynamic Configuration Adaptation**: Our scripts adapted to the dynamic nature of the cluster, handling varying VM names, IP addresses, and resource limits without manual intervention.
- **File Transfer and Task Synchronization**: Efficient file transfer and synchronization across VMs were achieved, ensuring seamless operation of distributed applications.

### Performance Optimization and Experimentation
- **Memcached Performance Under Interference**: We thoroughly evaluated the impact of different types of hardware resource interference (e.g., CPU, L1d, L1i, LLC, memory bandwidth) on memcached’s performance, measuring tail latency and saturation points under various conditions.
- **Batch Processing with PARSEC**: We evaluated how batch workloads from the PARSEC suite (e.g., `blackscholes`, `canneal`, `dedup`, etc.) performed under different resource constraints, optimizing their execution using Kubernetes scheduling policies.

### Scheduling Policies and Creative Solutions (Part 3 & 4)
- **Optimal Scheduling Policy**: We designed and tested an optimized scheduling policy that minimized latency for memcached while maximizing resource usage for batch jobs. This involved sophisticated job placement strategies and core/thread allocation for each workload.
- **Dynamic Core Allocation for Memcached**: Using a **controller** to monitor and dynamically adjust core allocations, we ensured that memcached met strict performance Service Level Objectives (SLOs) under varying loads.
- **Parallelization of Batch Jobs**: We implemented advanced scheduling techniques to parallelize jobs based on their resource dependencies, achieving an optimal balance between job execution time and system resource usage.

## Creative Highlights

- **Advanced Interference Management**: We creatively explored and documented the effect of multiple levels of cache and CPU interference on both **memcached** and **PARSEC workloads**. The insightful analysis led to innovative solutions in scheduling and core allocation to optimize performance.
- **SLO-Aware Dynamic Core Management**: One of the standout achievements in our project was the development of a **dynamic core allocation controller** that adjusted resources in real-time based on load conditions while strictly adhering to the performance SLO of memcached.
- **Detailed Experimentation**: Our extensive experiments involving multiple scenarios for memcached and batch job scheduling provided critical insights into workload behaviors, which led to data-driven optimization of resource management.

## Bash Scripts

We wrote all the **Bash code** from scratch to automate the entire process, including:
- **Cluster creation and teardown**.
- **Concurrency management**: Running commands in parallel across multiple nodes to speed up processes.
- **Dynamic adaptation**: Adapting to variable node names and IP addresses.
- **File transfers** between different virtual machines and nodes for smooth operation of the system.
- **Log collection and automated performance data retrieval**.

## Conclusion

This project reflects a deep understanding of cloud infrastructure, orchestration, and performance tuning. By focusing on automation, optimization, and experimentation, we developed a system capable of dynamically managing both latency-sensitive and batch applications at scale, while efficiently using cloud resources.

For more detailed technical information, please refer to the **project reports** included with this submission.

---

**Authors**  
Group 020  
- Ambroise Aigueperse  
- Témi Messmer  
- Monika Multani
