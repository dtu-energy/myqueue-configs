# Myqueue-for-HPC
[MyQueue](https://myqueue.readthedocs.io/en/latest/) is a program for submitting single jobs or maintaining jobs in a package in a HPC cluster or local machine. It supports SLURM,PBS,LSF.
To use MyQueue you need a configuration file specific to your HPC or local machine. Create a folder named `.myqueue` in your home directory and add a configurational file called `config.py` which consist of all the partitions in your HPC/local machine.
You can then, either download/clone the `config.py` file into your `.myqueue` directory, or just copy the contents of the file into a new `config.py` file.
When you have added your configuration file you can download MyQueue by the command `$ pip install myqueue`. To initiate MyQueue in a specific folder you need to write `$ mq init` in the terminal. It will then copy your `.myqueue` folder with the configuration file. Example `config.py` for a set of different HPC are presented in this repository.

### ASPIRE 2A (NSCC, PBS)

This cluster uses PBS Pro. Copy [`ASPIRE2A/config.py`](ASPIRE2A/config.py) to `~/.myqueue/config.py`. It submits to the `normal` routing queue with `-P personal`. Change the project in `extra_args` to your project ID when needed.

MyQueue needs Python ≥ 3.9. On ASPIRE 2A:

```bash
module load python/3.11.7-gcc11
python3 -m pip install --user myqueue
```

ASPIRE2A’s `qsub` does not support `-d`. Install the wrapper from this repo so MyQueue works (MyQueue always passes `-d`):

```bash
cp ASPIRE2A/qsub-wrapper ~/.local/bin/qsub
chmod +x ~/.local/bin/qsub
# ensure ~/.local/bin is before /opt/pbs/bin on PATH (default on this system)
```

Example submits:

```bash
mq submit script.py -R s:1:cpu:30m      # serial, 1 core
mq submit script.py -R 128:1:cpu:24h      # full CPU node
mq submit script.py -R 64:1:gpu:2h        # GPU node (special)
mq submit script.py -R 128:1:largemem:24h # large memory (special)
```

Now you can begin using MyQueue.

To submit jobs using MyQueue you need to write a command like `$ mq submit test.py -R 24:xeon24:2d`. This command will submit a python script called `test.py` in the `xeon24` partitions with 24 nodes for 2 days. To keep track of your jobs you can use the command `$ mq ls`, which list your jobs. You can delete jobs from the list by using `$ mq rm`. For more details about commands use `--help` after a command.
To learn more please see the [MyQueue documentation](https://myqueue.readthedocs.io/en/latest/).

Note: If you are experiencing issues with submitting a VASP or similar calculation, try instead of `xeon24:24:1h` adding `xeon24:24:1:1h`. This will start a single process instead of 24 processes.

