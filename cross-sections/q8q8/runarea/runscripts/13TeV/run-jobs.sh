#!/bin/bash
(trap 'kill 0' SIGINT; sleep 0s && bash job_1.sh & sleep 1s && bash job_2.sh & wait)
