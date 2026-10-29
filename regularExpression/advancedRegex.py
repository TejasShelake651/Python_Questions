import re

def main():
    sample_email = "virajpotdar4@gmail.com"
    print(f"Sample String: '{sample_email}'")

    # 1. re.findall
    words = re.findall(r"\w+", sample_email)
    print("re.findall(r'\\w+'):", words)

    # 2. re.compile and search
    pattern = re.compile(r"\w+@\w+\.\w+")
    compiled_match = pattern.search(sample_email)
    print("re.compile() + search():", compiled_match.group() if compiled_match else "No match")

    # 3. re.split
    parts = re.split(r"@", sample_email)
    print("re.split(r'@'):", parts)

    # 4. re.sub (Search & Replace)
    replaced = re.sub(r"gmail", "yahoo", sample_email)
    print("re.sub('gmail' -> 'yahoo'):", replaced)

    # 5. re.escape
    escaped = re.escape(sample_email)
    print("re.escape():", escaped)

    # 6. HTML Tag Removal
    html_text = "<p>This is a <b>bold</b> statement with <a href='#'>links</a>.</p>"
    clean_text = re.sub(r"<[^>]*>", "", html_text)
    print("\nHTML Tag Stripping:")
    print("Original:", html_text)
    print("Stripped:", clean_text)

    # 7. IPv4 and IPv6 Validator
    def validate_ip(ip):
        ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
        ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
        if re.match(ipv4_pattern, ip):
            parts = ip.split(".")
            if all(0 <= int(part) <= 255 for part in parts):
                return "Valid IPv4"
        elif re.match(ipv6_pattern, ip):
            return "Valid IPv6"
        return "Invalid IP"

    print("\nIP Address Validation:")
    for ip in ["192.168.1.1", "999.999.999.999", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]:
        print(f"  {ip}: {validate_ip(ip)}")

    # 8. Date and URL Extraction
    text_with_data = "Event on 15/08/2026 visit https://google.com and check #pythonlab"
    dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text_with_data)
    urls = re.findall(r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text_with_data)
    hashtags = re.findall(r"#[a-zA-Z0-9_]+", text_with_data)

    print("\nExtractions:")
    print("Dates found:", dates)
    print("URLs found:", urls)
    print("Hashtags found:", hashtags)


if __name__ == "__main__":
    main()
