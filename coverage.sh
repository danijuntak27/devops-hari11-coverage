#!/bin/bash

coverage run -m pytest
coverage report
coverage html  # Bisa dibuka manual pakai browser lokal kalau ingin
