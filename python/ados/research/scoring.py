def score(repo):

    total=(
        repo.architecture+
        repo.cli+
        repo.plugins+
        repo.memory+
        repo.testing+
        repo.docs
    )

    repo.total=total
    return total
