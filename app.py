import gradio as gr


def make_bar(crowd, max_crowd):
    # Create a simple text bar to visualize crowd size
    if max_crowd == 0:
        return ""
    length = int((crowd / max_crowd) * 20)
    return "█" * length


def format_final_result(sorted_stops):
    # Format the final ranked list
    text = "Shuttle Stop Crowd Ranking\n\n"
    for i, (stop, crowd) in enumerate(sorted_stops, start=1):
        text += f"{i}. {stop} - {crowd}\n"
    return text


def merge_sort_visual(stops):
    # This will store detailed information for each merge step
    steps = []
    working = stops[:]
    temp = [None] * len(working)

    def merge_sort_range(left, right):
        # A section with 0 or 1 item is already sorted
        if left >= right:
            return

        mid = (left + right) // 2

        # Recursively sort the left half and right half
        merge_sort_range(left, mid)
        merge_sort_range(mid + 1, right)

        # Merge the two halves
        merge(left, mid, right)

    def merge(left, mid, right):
        i = left
        j = mid + 1
        k = left

        # Merge the two sorted halves into temp
        while i <= mid and j <= right:
            if working[i][1] >= working[j][1]:
                temp[k] = working[i]
                i += 1
            else:
                temp[k] = working[j]
                j += 1
            k += 1

        # Copy any leftover items from the left half
        while i <= mid:
            temp[k] = working[i]
            i += 1
            k += 1

        # Copy any leftover items from the right half
        while j <= right:
            temp[k] = working[j]
            j += 1
            k += 1

        # Copy the merged section back into the main list
        for index in range(left, right + 1):
            working[index] = temp[index]

        # Save BOTH:
        # 1. the full current list
        # 2. the merged section only
        steps.append({
            "full_list": working[:],
            "merged_part": working[left:right + 1],
            "left": left,
            "right": right
        })

    if len(working) > 0:
        merge_sort_range(0, len(working) - 1)

    return working, steps


def format_step(step_index, steps):
    # Show one step with both full-list view and merged-part view
    if not steps:
        return "No steps to display."

    step = steps[step_index]
    full_list = step["full_list"]
    merged_part = step["merged_part"]
    left = step["left"]
    right = step["right"]

    max_crowd_full = max(crowd for _, crowd in full_list) if full_list else 0
    max_crowd_part = max(crowd for _, crowd in merged_part) if merged_part else 0

    text = f"Step {step_index + 1} of {len(steps)}\n\n"

    text += "Full List at This Step:\n"
    for i, (stop, crowd) in enumerate(full_list, start=1):
        bar = make_bar(crowd, max_crowd_full)
        text += f"{i}. {stop:20} {crowd:3}  {bar}\n"

    text += "\n"
    text += f"Merged Part Only (positions {left + 1} to {right + 1}):\n"
    for stop, crowd in merged_part:
        bar = make_bar(crowd, max_crowd_part)
        text += f"{stop:20} {crowd:3}  {bar}\n"

    return text


def sort_bus_stops(user_input):
    # Make sure the user entered something
    if user_input.strip() == "":
        return "Please enter bus stop data.", "No steps to display.", [], 0

    lines = user_input.strip().split("\n")
    bus_stops = []

    # Read and validate each line
    for line_number, line in enumerate(lines, start=1):
        parts = line.split(",")

        if len(parts) != 2:
            return f"Line {line_number} is invalid. Use: stop name, crowd count", "No steps to display.", [], 0

        stop_name = parts[0].strip()
        crowd_text = parts[1].strip()

        if stop_name == "":
            return f"Line {line_number}: bus stop name cannot be empty.", "No steps to display.", [], 0

        try:
            crowd_count = int(crowd_text)
        except ValueError:
            return f"Line {line_number}: crowd count must be a whole number.", "No steps to display.", [], 0

        if crowd_count < 0:
            return f"Line {line_number}: crowd count cannot be negative.", "No steps to display.", [], 0

        bus_stops.append((stop_name, crowd_count))

    # Run merge sort and collect step data
    sorted_stops, steps = merge_sort_visual(bus_stops)

    final_result = format_final_result(sorted_stops)

    if steps:
        step_text = format_step(0, steps)
        step_index = 0
    else:
        step_text = "No steps to display."
        step_index = 0

    return final_result, step_text, steps, step_index


def next_step(steps, step_index):
    # Move forward one step if possible
    if not steps:
        return "No steps to display.", step_index

    if step_index < len(steps) - 1:
        step_index += 1

    return format_step(step_index, steps), step_index


def previous_step(steps, step_index):
    # Move backward one step if possible
    if not steps:
        return "No steps to display.", step_index

    if step_index > 0:
        step_index -= 1

    return format_step(step_index, steps), step_index


with gr.Blocks() as demo:
    gr.Markdown("# Shuttle Stop Crowd Ranking")
    gr.Markdown("Enter one bus stop per line in this format: `stop name, crowd count`")

    input_box = gr.Textbox(
        label="Bus Stop Input",
        lines=8,
        value="Main Gate, 42\nLibrary, 15\nDorms, 33\nScience Building, 24\nGym, 18"
    )

    sort_button = gr.Button("Sort Stops")

    result_box = gr.Textbox(label="Final Result", lines=8)
    step_box = gr.Textbox(label="Step Viewer", lines=18)

    with gr.Row():
        prev_button = gr.Button("Previous Step")
        next_button = gr.Button("Next Step")

    steps_state = gr.State([])
    step_index_state = gr.State(0)

    sort_button.click(
        fn=sort_bus_stops,
        inputs=input_box,
        outputs=[result_box, step_box, steps_state, step_index_state]
    )

    next_button.click(
        fn=next_step,
        inputs=[steps_state, step_index_state],
        outputs=[step_box, step_index_state]
    )

    prev_button.click(
        fn=previous_step,
        inputs=[steps_state, step_index_state],
        outputs=[step_box, step_index_state]
    )

demo.launch()