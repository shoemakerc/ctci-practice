# power_set.py

def generate_power_set(input):
	def directed_power_set(to_be_selected, selected_so_far):
		if to_be_selected == len(input):
			power_set.append(list(selected_so_far))
			return
		directed_power_set(to_be_selected + 1, selected_so_far)
		directed_power_set(to_be_selected + 1, selected_so_far + [input[to_be_selected]])
	power_set = []
	directed_power_set(0, [])
	return power_set

def main():
	input = [0, 1, 2]
	print(generate_power_set(input))
main()