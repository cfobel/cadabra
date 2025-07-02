#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail

pixi init --format pyproject
(cd frontend && pnpm init --yes)
