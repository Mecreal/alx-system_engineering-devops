# Web Stack Debugging #3

## Project Description

This project is part of the ALX System Engineering & DevOps curriculum. The goal is to debug a Wordpress website running on a LAMP stack (Linux, Apache, MySQL, and PHP) using `strace` and then automate the fix using Puppet.

## Task: Strace is your friend

### Objective
Find out why Apache is returning a 500 error using `strace`, fix the issue, and automate the solution using Puppet.

### Requirements
- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- Puppet manifests must run without error
- Puppet manifests' first line must be a comment explaining the manifest's purpose
- Puppet manifest files must end with the extension .pp
- Files will be checked with Puppet v3.4

### File
- `0-strace_is_your_friend.pp`: Contains the Puppet code to fix the issue

## Installation

To install `puppet-lint`:

```bash
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
```

## Usage

1. Run `strace` on the Apache process to identify the issue
2. Fix the issue manually
3. Create a Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix
4. Apply the Puppet manifest:
   ```
   puppet apply 0-strace_is_your_friend.pp
   ```

## Testing

After applying the Puppet manifest, you can test the fix by running:

```bash
curl -sI 127.0.0.1
```

The expected output should be a 200 OK status instead of a 500 Internal Server Error.

## Author

Hamza Abouabid

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.