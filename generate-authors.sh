#!/usr/bin/env bash
set -e

{
	cat <<- 'EOH'
		# This file lists all M*Éividuals having contributed content to the repository.
		# For how it is generated, see `hack/generate-authors.sh`.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
