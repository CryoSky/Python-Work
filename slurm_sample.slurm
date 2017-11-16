#!/bin/bash
#SBATCH --job-name=20171022Gromacstest1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --threads-per-core=1
#SBATCH --mem-per-cpu=1000m
#SBATCH --time=24:00:00
#SBATCH --export=ALL
#SBATCH --mail-user=Shikai.Jin@rice.edu
#SBATCH --mail-type=ALL
#SBATCH --output=batch_test_%A_%a.out
#SBATCH --nodes=1
#SBATCH -e trial.err



module load icc/2015.2.164 ifort/2015.2.164 iomkl/2015.02.1 OpenMPI/1.8.8
/scratch/sj52/gmx504-ryan-v8.1_CRSERAL/bin/gmx_avx mdrun -s $SLURM_SUBMIT_DIR/run.tpr -noddcheck -maxh 20
