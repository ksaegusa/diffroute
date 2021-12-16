# routediff

```
ansible-galaxy role install https://github.com/ksaegusa/routediff.git
```

```example1.yml
- name: RouteDiff
  hosts: localhost
  gather_facts: false

  tasks:
    - name: RouteDiff(diff)
      import_role:
        name: routediff
        tasks_from: diff
      vars:
        before_ip_route: "{{ lookup('file', 'before_ip_route.txt') }}"
        after_ip_route: "{{ lookup('file', 'after_ip_route.txt') }}"
```

```example2.yml
- name: RouteDiff
  hosts: localhost
  gather_facts: false

  tasks:
    - name: RouteDiff(sortdiff)
      import_role:
        name: routediff
        tasks_from: sortdiff
      vars:
        before_ip_route: "{{ lookup('file', 'before_ip_route.txt') }}"
        after_ip_route: "{{ lookup('file', 'after_ip_route.txt') }}"
```

`Difference route`
```
# Result
  +{'PROTOCOL': 'D', 'TYPE': '', 'NETWORK': '10.0.4.0', 'MASK': '26', 'DISTANCE': '90', 'METRIC': '2297856', 'NEXTHOP_IP': '10.0.1.2', 'NEXTHOP_IF': 'Serial0/0'}

```

`Not Difference route`
```
# Result
  Not Difference

```