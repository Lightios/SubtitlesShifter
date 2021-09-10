def gen():
	try:
		for i in open("Example subtitles.srt", 'r', encoding="utf-8").readlines():
			yield i
	except FileNotFoundError:
		return

class Time:
	def __init__(self, line):
		self.hours = int(line[0:2])
		self.minutes = int(line[3:5])
		self.seconds = int(line[6:8])
		self.milliseconds = int(line[9:12])

	def __str__(self):
		return f"{self.hours}:{self.minutes}:{self.seconds},{self.milliseconds}"

	def calculate(self, shift):
		"""
		Calculates new values after shifitng
		"""
		if shift > 0:
			if self.seconds + shift >= 60:
				self.minutes += 1
				if self.minutes >= 60:
					self.hours += 1
					self.minutes %= 60

		else:
			if self.seconds + shift < 0:
				self.minutes -= 1
				if self.minutes < 0:
					self.hours -= 1
					self.minutes += 60

		self.seconds = (self.seconds + shift) % 60

	def back_to_string(self):
		"""
		Formates data back to string, adds 0 if values are less than 10
		"""
		if self.seconds < 10:
			self.seconds = f"0{self.seconds}"

		if self.minutes < 10:
			self.minutes = f"0{self.minutes}"

		if self.hours < 10:
			self.hours = f"0{self.hours}"


if __name__ == '__main__':
	# time in seconds to shift subtitles (can be negative)
	SHIFT = 53
	# set to True if you want to see output for each line
	SHOW_OUTPUT = False

	# reads data
	data = gen()
	with open("formatted.srt", "w", encoding="utf-8") as file:
		for line in data:
			# if line starts with letter, it will only rewrite it
			try:
				int(line[0])
			except ValueError:
				file.write(line)
				continue

			# skip lines with text number
			if len(line) > 5:
				line = line.split()

				t1 = Time(line[0])
				if SHOW_OUTPUT:
					print("******************************")
					print(t1)

				t1.calculate(SHIFT)

				if SHOW_OUTPUT:
					print(t1)

				t1.back_to_string()

				if SHOW_OUTPUT:
					print(t1)

				t2 = Time(line[2])
				if SHOW_OUTPUT:
					print("******************************")
					print(t2)

				t2.calculate(SHIFT)

				if SHOW_OUTPUT:
					print(t2)

				t2.back_to_string()

				if SHOW_OUTPUT:
					print(t2)

				file.write(f"{t1} {line[1]} {t2}\n")
			else:
				file.write(line)