{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = with pkgs; [
    git
    python311
    python311Packages.pip
    python311Packages.setuptools
    python311Packages.virtualenv
  ];
  shellHook = ''
    virtualenv .venv
    source .venv/bin/activate
    export PYTHONPATH=`pwd`/.venv/python3.11/site-packages/
    pip3 install -e .
  '';
}
