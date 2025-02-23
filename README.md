# IP List Generator

## Description

This Python script generates a list of IP addresses based on various input formats. Users can specify IPs using CIDR notation, comma-separated values, or dash-separated ranges. Additionally, the script allows users to exclude specific IPs from the generated list.

## Features

Accepts IP addresses in CIDR, comma-separated, or range format.

Allows exclusion of specific IPs using the same formats.

Outputs the final list of sorted IPs to a specified file.

Ensures proper numerical sorting of IP addresses.

## Requirements

Python 3.x

## Usage

### Run the script with the following options:

```text
python hlm.py -t <targets> -o <output_file> [-e <exclusions>]
```
```bash
python3 hlm.py -t <targets> -o <output_file> [-e <exclusions>]
```

### Arguments

`-t`, `--targets` (required): Specifies target IPs using CIDR notation, comma-separated values, or range format.

`-e`, `--exclude` (optional): Specifies IPs to exclude using CIDR notation, comma-separated values, or range format.

`-o`, `--output` (required): Specifies the output file name.

`-h`, `--help`: Displays the help message.

### Examples

Generate a list from a CIDR block

```text
python hlm.py -t 192.168.1.0/30 -o output.txt
```
```bash
python3 hlm.py -t 192.168.1.0/30 -o output.txt
```

Output file content:

```text
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
```

Combine multiple CIDRs:

```text
python hlm.py -t 192.168.1.0/29,10.0.0.0/30 -o output.txt
```
```bash
python3 hlm.py -t 192.168.1.0/29,10.0.0.0/30 -o output.txt
```

Output file content:

```text
10.0.0.0
10.0.0.1
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
```

Mix CIDR, ranges, and comma-separated IPs:

```text
python hlm.py -t 192.168.1.0/29,10.0.0.10-12,172.16.0.1,192.168.2.1 -o output.txt
```
```bash
python3 hlm.py -t 192.168.1.0/29,10.0.0.10-12,172.16.0.1,192.168.2.1 -o output.txt
```

Output file content:

```text
10.0.0.10
10.0.0.11
10.0.0.12
172.16.0.1
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
192.168.2.1
```

Generate a list with a range

```text
python hlm.py -t 192.168.1.10-12 -o output.txt
```
```bash
python3 hlm.py -t 192.168.1.10-12 -o output.txt
```

Output file content:

```text
192.168.1.10
192.168.1.11
192.168.1.12
```

Exclude specific IPs

```text
python hlm.py -t 192.168.1.0/29 -e 192.168.1.2,192.168.1.3 -o output.txt
```
```bash
python3 hlm.py -t 192.168.1.0/29 -e 192.168.1.2,192.168.1.3 -o output.txt
```

Output file content:

```text
192.168.1.0
192.168.1.1
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
```

Combine multiple exclusions:

```text
python hlm.py -t 192.168.1.0/29,10.0.0.0/30 -e 192.168.1.2-3,10.0.0.1 -o output.txt
```
```bash
python3 hlm.py -t 192.168.1.0/29,10.0.0.0/30 -e 192.168.1.2-3,10.0.0.1 -o output.txt
```

Output file content:

```text
10.0.0.0
192.168.1.0
192.168.1.1
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
```

## License

This project is open-source and available under the MIT License.
