import concurrent.futures
import subprocess

def find_function_info(function_list_file, output_file):
    with open(function_list_file, 'r') as f_in:
        function_list = f_in.read().splitlines()

    def process_function(function):
        address = function.split()[0].split("::")[1]
        cmd = "grep 'struct "+ address + " {' -nR"
        print(cmd)
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode("utf-8")
            source_info = result
            # print(source_info)
            for i in result.strip().split("^\n"):
                print(i.split(":"))
                    # print(j[0])
            # source_info = result.strip().split()[-1]  # Extract the last part (source file:line number)
        except subprocess.CalledProcessError as e:
            source_info = "ERROR: {}".format(e.output.decode('utf-8').strip())

        return source_info

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_function, function_list))

    with open(output_file, 'w') as f_out:
        for source_info in results:
            line = "{}\n".format(source_info)  # Only write the source file and line number
            f_out.write(line)

if __name__ == "__main__":
    function_list_file = "rust_wrapped_structers2.txt"
    # vmlinux_file = "vmlinux"
    output_file = "rust_wrapped_structers_info.txt"

    find_function_info(function_list_file, output_file)
