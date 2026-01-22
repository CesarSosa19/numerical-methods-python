def errors(actual, anterior):
    errAbs = abs(actual - anterior)

    if actual != 0:
        errRel = errAbs / abs(actual)
    else:
        errRel = float('inf')

    return errAbs, errRel
