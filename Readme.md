[![tests](https://github.com/boutetnico/ansible-role-swap/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-swap/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.swap-blue.svg)](https://galaxy.ansible.com/boutetnico/swap)

ansible-role-swap
=================

This role configures Linux swap.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default                 | Choices   | Comments                            |
|------------------------------|----------|-------------------------|-----------|-------------------------------------|
| swap_dependencies            | yes      | `[procps,util-linux]`   | list      |                                     |
| swap_enabled                 | yes      | `true`                  | bool      |                                     |
| swap_size                    | yes      | `1G`                    | string    |                                     |
| swap_file                    | yes      | `/swap`                 | string    |                                     |
| swap_swappiness              | no       |                         | int       |                                     |
| swap_vfs_cache_pressure      | no       |                         | int       |                                     |

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
