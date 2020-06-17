#!/bin/bash

#DEV

# add ssh keys to chain
ssh-add -k ~/.ssh/authorized_keys/devgitlabrunner.pem
ssh-add -k ~/.ssh/authorized_keys/bastion-default.pem

# connect to the bastion box (with -A, ssh-agent forwarding)
ssh -A centos@ec2-18-222-109-155.us-east-2.compute.amazonaws.com

# (from jump box to aws box):
# ssh ec2-user@192.168.1.165
