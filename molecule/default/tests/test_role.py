import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('util-linux'),
  ('procps'),
])
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('file,user,group,mode', [
  ('/swapfile_test', 'root', 'root', 0o600),
])
def test_swap_file_exist(host, file, user, group, mode):
    swap = host.file(file)
    assert swap.exists
    assert swap.is_file
    assert swap.user == user
    assert swap.group == group
    assert swap.mode == mode


@pytest.mark.parametrize('key,expected_value', [
  ('vm.swappiness', 10),
  ('vm.vfs_cache_pressure', 400),
])
def test_sysctl_values(host, key, expected_value):
    value = host.sysctl(key)
    assert expected_value == value
