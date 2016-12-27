#!/usr/bin/python3

import dns.resolver

domain = input('please input an domain: ')
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        print(j)
