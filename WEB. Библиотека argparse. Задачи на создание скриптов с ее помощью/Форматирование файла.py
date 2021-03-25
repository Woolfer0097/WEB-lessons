import argparse


def format_text_block(frame_height, frame_width, file_name):
    result_data = []
    with open(file_name, "r", encoding='utf-8') as file:
        data = file.read().splitlines()
    num_line = 0
    for line in data:
        for i in range(0, len(line), frame_width):
            if "\n" not in line:
                result_data.append(f"{line[i:i + frame_width]}")
                num_line += 1
                if num_line > frame_height:
                    return result_data
            else:
                result_data.append("\n")
                num_line += 1
                if num_line > frame_height:
                    return result_data
    # for y in range(frame_height):
    #     temp_data = []
    #     for x in range(frame_width):
    #         temp_data.append(data[x])
    #     result_data.append(["".join(temp_data)])
    # print(result_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', nargs='*')
    parser.add_argument('--frame-height', nargs="?")
    parser.add_argument('--frame-width', nargs="?")
    args = parser.parse_args()
    print("\n".join(format_text_block(int(args.frame_height), int(args.frame_width), *args.arg)))
