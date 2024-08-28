# SSH Project

This project focuses on understanding and implementing SSH (Secure Shell) concepts. It includes tasks related to connecting to a remote server, creating SSH key pairs, and configuring SSH clients.

## Project Structure

- `0-use_a_private_key`: Bash script to connect to a server using a private key
- `1-create_ssh_key_pair`: Bash script to create an RSA key pair
- `2-ssh_config`: SSH client configuration file
- Additional files for other tasks

## Requirements

- All scripts are interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- All Bash script files must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Tasks

1. Use a private key
2. Create an SSH key pair
3. Client configuration file
4. Let me in!

## How to Use

Each script can be run independently. Make sure to set the correct permissions before executing:

```bash
chmod +x script_name.sh
./script_name.sh
```

For the SSH configuration file, place it in the appropriate directory (usually `~/.ssh/config`).

## Author

ABOUABID Hamza

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.