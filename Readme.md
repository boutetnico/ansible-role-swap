ansible-role-swap
=================

This role configures Linux swap.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| swap_dependencies            | yes      | `[procps,util-linux]`           | list      |                                               |
| swap_enabled                 | yes      | `true`                          | bool      |                                               |
| swap_size                    | yes      | `1G`                            | string    |                                               |
| swap_file                    | yes      | `/swap`                         | string    |                                               |
| swap_swappiness              | no       |                                 | int       |                                               |
| swap_vfs_cache_pressure      | no       |                                 | int       |                                               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-swap

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
