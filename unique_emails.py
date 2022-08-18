def unique_emails(emails):
    unique = set()
    for e in emails:
        i = e.index('@')
        local = e[:i]
        domain = e[i:]
        if '+' in local:
            plus = local.index('+')
            local = local[:plus]
        newlocal = ''
        for l in local:
            if l != '.':
                newlocal += l
        unique.add(newlocal + domain)
    return len(unique)
