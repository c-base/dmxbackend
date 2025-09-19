{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  packages = [
    pkgs.python3
    pkgs.nodejs_20
    pkgs.git
  ];

}
