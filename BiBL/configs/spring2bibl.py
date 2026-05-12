def extract_amr_data(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    output_lines = []
    buffer = []
    in_graph = False

    for line in lines:
        if line.startswith("# ::snt"):
            # If a previous example exists, flush it
            if buffer:
                output_lines.extend(buffer)
                output_lines.append("")  # blank line between examples
                buffer = []
            buffer.append(line)  # keep ::snt line
            in_graph = True

        elif line.startswith("#") and not (line.startswith("# ::alignment") or line.startswith("# ::document")):
            continue  # skip other metadata comments but keep alignment/document

        elif line == "":
            continue  # skip stray empty lines

        elif line == "# ::source UMRV2":
            continue

        elif in_graph:
            # Keep AMR graph and any non-comment lines that follow
            buffer.append(line)

    # Add the last entry
    if buffer:
        output_lines.extend(buffer)
        output_lines.append("")

    # Write to output file
    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write("".join(output_lines))

    print(f"Formatted data written to: {output_path}")


# Usage
if __name__ == "__main__":
    #input_file = "/home/common/ACNLP/umr_generation/umr_data/train/doc/eng_doc_train_spring.txt"
    input_file = '/home/common/ACNLP/umr_parsing/umr2_data/train/sent/eng-sent-spring-dev2.txt'
    output_file = "/home/common/ACNLP/umr_parsing/umr2_data/train/sent/eng-sent-bibl-dev2.txt"
    extract_amr_data(input_file, output_file)
