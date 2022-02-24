class AnsibleKeyring < Formula
  desc "A CLI that extends ansible, ansible-playbook, and ansible-vault to use the system keyring for vault passwords"
  homepage "https://megabyte.space"
  url "https://github.com/ProfessorManhattan/ansible-keyring/releases/download/v1.1.0/ansible-keyring.tar.gz"
  version "1.1.0"
  license "MIT"

  

  def install
    os = OS.kernel_name.downcase
    arch = Hardware::CPU.intel? ? "amd64" : Hardware::CPU.arch.to_s
    bin.install "build/bin/ansible-keyring-#{os}_#{arch}" => "ansible-keyring"
  done

  test do
    system bin/"ansible-keyring", "--version"
  end
end
