import argparse
import ipaddress

def parse_range(range_str):
    """Parse a single IP range or a single IP."""
    if '-' in range_str:
        start, end = range_str.split('-')
        start_ip = ipaddress.IPv4Address(start)

        # If end is a full IP, use it directly
        if '.' in end:
            end_ip = ipaddress.IPv4Address(end)
        else:
            # Assume only the last octet was provided
            start_octets = start.split('.')
            end_ip = ipaddress.IPv4Address('.'.join(start_octets[:-1] + [end]))

        # Convert IPs to integers, calculate the range, and then convert back to IPs
        start_int = int(start_ip)
        end_int = int(end_ip)

        return [str(ipaddress.IPv4Address(ip)) for ip in range(start_int, end_int + 1)]

    else:
        return [range_str]

def parse_targets(targets):
    """Parse multiple targets from CIDR, comma-separated, or range formats."""
    ips = set()
    for target in targets.split(','):
        target = target.strip()
        if '/' in target:
            ips.update(map(str, ipaddress.IPv4Network(target, strict=False).hosts()))
        else:
            ips.update(parse_range(target))
    return ips

def main():
    parser = argparse.ArgumentParser(description="Generate an IP list from different formats.")
    parser.add_argument('-t', '--targets', required=True, help="Target IPs in CIDR, comma-separated, or range format.")
    parser.add_argument('-e', '--exclude', help="Exclude IPs in CIDR, comma-separated, or range format.")
    parser.add_argument('-o', '--output', required=True, help="Output file to save the results.")

    args = parser.parse_args()

    target_ips = parse_targets(args.targets)
    exclude_ips = parse_targets(args.exclude) if args.exclude else set()

    final_ips = sorted(target_ips - exclude_ips, key=lambda ip: tuple(map(int, ip.split('.'))))

    with open(args.output, 'w') as f:
        f.write('\n'.join(final_ips) + '\n')

    print(f"Generated {len(final_ips)} IPs and saved to {args.output}")

if __name__ == "__main__":
    main()
