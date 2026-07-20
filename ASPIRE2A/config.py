# NSCC ASPIRE 2A (PBS Pro)
# Submit to the "normal" routing queue; PBS picks q1–q6 / qlong / … from resources.
# Change -P to your project ID (e.g. '11001786') when not using personal.

config = {
    'scheduler': 'pbs',
    'mpiexec': 'mpiexec',
    # Use mq-python under mpiexec so Cray PALS does not realpath away the venv
    'serial_python': '/home/users/ntu/martinpe/postdoc/bin/mq-python',
    'parallel_python': '/home/users/ntu/martinpe/postdoc/bin/mq-python',
    'extra_args': ['-q', 'normal', '-P', 'personal'],
    'nodes': [
        # Standard CPU node: 128 cores, ~440 GB RAM
        ('cpu', {
            'cores': 128,
            'memory': '440G',
            # mem must be a separate -l (not inside nodes=…:ppn=…) on this PBS
            'extra_args': ['-l', 'mem=400gb'],
        }),
        # Large-memory CPU (routes to l1/l2/l3 by mem request)
        ('largemem', {
            'cores': 128,
            'memory': '2000G',
            'special': True,
            'extra_args': ['-l', 'mem=2000gb'],
        }),
        # GPU node: 64 cores, 4 GPUs — request explicitly: -R 64:gpu:…
        ('gpu', {
            'cores': 64,
            'memory': '440G',
            'special': True,
            'extra_args': ['-l', 'mem=400gb', '-l', 'ngpus=4'],
        }),
    ],
}
