import subprocess


def login(profile_name):
    try:
        print(f"Logging in with profile: {profile_name}")
        subprocess.run(
            ['aws', 'sso', 'login', '--profile', profile_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error logging in: {e}")
        print(e.stderr.decode('utf-8'))
        return False

    return True
