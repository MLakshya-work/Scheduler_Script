import paramiko

def ssh_run_command_and_fetch_data():
    remote_host = "139.84.136.168"
    remote_user = "root"  # Replace with the actual username

    # Set up SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically accept unknown keys

    sftp = None  # Initialize sftp variable outside try block to avoid UnboundLocalError

    try:
        # Connect to the remote server using SSH key
        print("Connecting to remote server...")
        # SSH will automatically use the default private key (~/.ssh/id_rsa or ~/.ssh/id_ed25519)

        client.connect(remote_host, username=remote_user)  # No need for password or private key path

        # Define the directory and script to run
        remote_directory = "/root/dkron-scheduler-retriever"
        remote_script = f"cd {remote_directory} && python3 main.py"

        # Execute the command to run the script
        print("Running the script on the remote server...")
        stdin, stdout, stderr = client.exec_command(remote_script)

        # Capture the output (stdout) and errors (stderr)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        if output:
            print("Script output:", output)
        if error:
            print("Error:", error)

        # Now download the generated dkron_jobs.json
        print("Downloading the dkron_jobs.json file...")
        sftp = client.open_sftp()  # Initialize the SFTP session here
        remote_file_path = f"{remote_directory}/dkron_jobs.json"
        local_file_path = "dkron_jobs.json"

        # Download the file from the remote server to the local machine
        sftp.get(remote_file_path, local_file_path)
        print(f"Downloaded {remote_file_path} to {local_file_path}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            # Check if the SFTP session was initialized before trying to close it
            if sftp:
                sftp.close()
                print("SFTP session closed.")
        except Exception as sftp_error:
            print(f"Error closing SFTP session: {sftp_error}")
        
        # Close the SSH connection
        client.close()
        print("SSH connection closed.")

if __name__ == "__main__":
    ssh_run_command_and_fetch_data()

