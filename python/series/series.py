def slices(series, length):
    if length > len(series):
        raise ValueError('Length of subset cannot be larger than the one of the main set.')
    elif length < 1:
        raise ValueError('Length of subset cannot be 0 or negative')
    else:
        return [series[i:i+length] for i in range(len(series)-length+1)]
