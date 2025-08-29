from colorama import Fore, Style

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines = len(lines)
            total_words = sum(len(line.split()) for line in lines)

            print(Fore.CYAN + "📄 File Analysis Report" + Style.RESET_ALL)
            print(Fore.YELLOW + "-" * 30 + Style.RESET_ALL)
            print(Fore.GREEN + f"📌 Total Lines : {total_lines}")
            print(f"📝 Total Words : {total_words}" + Style.RESET_ALL)
            print(Fore.YELLOW + "-" * 30 + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + f"❌ Error: The file '{filename}' was not found." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"⚠️ An unexpected error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    read_file('sample.txt')
