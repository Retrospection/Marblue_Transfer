export function addRecord(url, qqNumber, fromGroup, toGroup) {
    return fetch(url, {
        method: 'POST',
        headers: {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'content-type': 'application/json'
        },
        body: JSON.stringify({
            'qq_number': qqNumber,
            'from_group': fromGroup,
            'to_group': toGroup
        }),
        mode: 'cors',
    }).then(response => response.json()) // parses response to JSON
}

export function query(url, qqNumber, startDate, endDate) {
    let body = {}
    if (qqNumber) {
        body.qq_number = qqNumber
    }
    if (startDate && endDate) {
        body.start_date = startDate
        body.end_date = endDate
    }
    return fetch(url, {
        method: 'POST',
        headers: {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
            'content-type': 'application/json'
        },
        body: JSON.stringify(body),
        mode: 'cors',
    }).then(response => response.json())
}