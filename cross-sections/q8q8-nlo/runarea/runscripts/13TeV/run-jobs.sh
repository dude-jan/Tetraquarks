#!/bin/bash
(trap 'kill 0' SIGINT; sleep 0s && bash job_1.sh & wait)
