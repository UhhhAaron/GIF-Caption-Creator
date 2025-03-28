# Image Setup

__Fill = Config["Settings"]["Caption_Design"]["Colors"]["Text"]
__Pasted_Color = Config["Settings"]["Caption_Design"]["Colors"]["Caption_Field"]

if Config["Settings"]["Dark_Mode"]["Enabled"]:
	if datetime.now().hour >= Config["Settings"]["Dark_Mode"]["After_Hour"]:
		__Fill = Config["Settings"]["Dark_Mode"]["Colors"]["Text"]
		__Pasted_Color = Config["Settings"]["Dark_Mode"]["Colors"]["Caption_Field"]

__Fill = Color(__Fill).hex_l
__Pasted_Color = Color(__Pasted_Color).hex_l

Image_Base = Image.new(
	"RGBA",
	(1250, 5000),
	(0,) * 4
)
Draw = ImageDraw.Draw(Image_Base)

# Automatic Max Width

Config["Media"]["Image"]["Max_Width"] = 1_000

# Font Setup

__Font_Size = Percentage(Config["Media"]["Image"]["Max_Width"], 10)
__Fonts = {Keys + 1: Values for Keys, Values in enumerate(
		[File[:-4] for File in sorted(
			next(os.walk("Fonts"))[2], key = str
		) if File.upper().endswith(("TTF", "OTF"))][::-1]
	)
}

if not Config["Text"]["Font"]["Type"]:
	Config["Text"]["Font"]["Type"] = randint(1, len(__Fonts))
__Path = "./Fonts/{0}.otf".format(__Fonts[Config["Text"]["Font"]["Type"]])
Font = ImageFont.truetype(__Path, __Font_Size)

# Emoji Setup

if Config["Text"]["Font"]["Type"] == 1:
	if Config["Emoji"]["API_Type"] == 1:
		if not Config["Emoji"]["Style_if_1"]:
			__Style = 3
		else:
			__Style = Config["Emoji"]["Style_if_1"]
	if Config["Emoji"]["API_Type"] == 2:
		__Style = {"Google": "7.1"}
		Get_Emoji_Image = Get_Emoji_Image2

if Config["Text"]["Font"]["Type"] == 2:
	if Config["Emoji"]["API_Type"] == 1:
		if not Config["Emoji"]["Style_if_1"]:
			__Style = 6
		else:
			__Style = Config["Emoji"]["Style_if_1"]
	if Config["Emoji"]["API_Type"] == 2:
		__Style = {"Twitter": "14.0"}
		Get_Emoji_Image = Get_Emoji_Image2

# Text CLI input

if not Config["Text"]["Content"]:
	print("\n{0}Warning{3}: {1}No text given!{3}\nPlease input.\n\nPerform {2}CTRL{3} + {2}C{3}, then {2}Enter{3} when done.\nPress {2}CTRL{3} + {2}Z{3}, then {2}Enter{3} to exit.\n\nText will be stripped. Multilne supported. ({2}Enter{3})\n{4}".format(
		Styles.Warning, Styles.Flaw, Styles.Info, Styles.Reset, __BEL
		)
	)

	try:
		ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
		ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
	except AttributeError:
		pass

	Lines = []
	while 1:
		try:
			Line = input("{0}> {1}".format(Styles.OK, Styles.Reset))
			Lines.append(Line)
		except KeyboardInterrupt:
			break
		except EOFError:
			raise SystemExit("Exiting.")
	if Lines:
		Lines = "\n".join(Lines).replace("\n", ". ")
		Config["Text"]["Content"] = Lines.rstrip(".") # You may input 2 dots in text instead
	else:
		raise SystemExit("No text inputted - exiting.")
	print("Finishing text input{0}\n".format("!" if Lines else " - Generating empty caption."))
	Config["Text"]["Content"] = "".join(Lines)

Config["Text"]["Content"] = emojize(Config["Text"]["Content"], use_aliases = 1)
Config["Text"]["Content"] = Replace(Config["Text"]["Content"], Config["Text"]["Replacements"])
Config["Text"]["Content"] = Config["Text"]["Content"].strip().strip("\n")
if Config["Text"]["Content"] == "":
	Config["Text"]["Content"] = "あ"

# Automatic Text Wrap

Text = wrap(
	"{0}".format(Config["Text"]["Content"]),
	width = 22
)

#print(Text)

#Text = wrap(
#	"{0}".format(Config["Text"]["Content"]),
#	width = Font.getsize(
#		sorted(Text, key = len)[-1])[0] - int(Config["Text"]["Additional_Wrap"] * 2
#	)
#)

Text = list(sum([Word.split(r"\n") for Word in Text], []))

# Caption Setup

Images = []
Expanded_Images = []
for Line in Text:
	width, height = Font.getbbox("x")[2], Font.getbbox("pÓ")[3]
	Line_Image = Image.new(
		"RGBA", (width * len(Line) * 2, height * 2)
	)
	Line_ImageDraw = ImageDraw.Draw(Line_Image)
	__X = 0
	#-=-=-=-#
	for Character in Line:
		if Character in UNICODE_EMOJI_ENGLISH:
			try:
				Emoji = Get_Emoji_Image(
					demojize(Character),
					__Style,
				)
			except UnidentifiedImageError as Error:
				raise SystemExit("{0}: The `{1}` emoji is not supported on this style. Image processing aborted.".format(
					Error.__class__.__name__,
					demojize(Character),
					)
				)
			#-=-=-=-#
			Emoji = Emoji.resize(
				(
					Percentage(
						Font.getbbox("pÓ")[3], 75
					),
				) * 2, 1
			)
			#-=-=-=-#
			Line_Image.paste(
				Emoji,
				(
					__X,
					Font.getbbox("p")[3] - Font.getbbox("o")[3], 
				),
				Emoji
			)
			__X += Emoji.size[0] + Config["Text"]["Kerning"]
			Character = Character.replace(Character, "")
		#-=-=-=-#
		Line_ImageDraw.text(
			xy = (__X, 5),
			text = Character,
			font = Font,
			fill = __Fill
		)
		#-=-=-=-#
		__X += Font.getbbox(Character)[2] + Config["Text"]["Kerning"]
		#-=-=-=-#
	Line_Image = Line_Image.crop(Line_Image.getbbox())

	Line_Image_2 = Image.new(
		Line_Image.mode,
		(
			Line_Image.size[0],
			Font.getbbox("yÓ")[3] + 5
		)
	)
	Line_Image_2.paste(Line_Image, (0, 0), Line_Image)
	#Line_Image_2 = ImageOps.expand(Line_Image_2, border = 1, fill= "#000") # Debug
	Images.append(Line_Image_2)
# Text Alignment
for IMG in enumerate(Images):
	IMG = IMG[0]
	Text_Image = Image.new(
		"RGBA",
		(
			Images[IMG].size[0],
			Images[IMG].size[1] + Font.getbbox("yÓ")[3] + len(Images) * 10
		),
		(0,) * 4
	) # Bug
	Text_Image.paste(
		Images[IMG],
		(
			0,
			Font.getbbox("yÓ")[3]
		),
		Images[IMG]
	)
	Expanded_Images.append(Text_Image)

__Y = 0
for IMG in enumerate(Expanded_Images):
	IMG = IMG[0]
	if IMG == len(Expanded_Images):
		__Y += Expanded_Images[0].size[1] // len(Expanded_Images)
	else:
		__Y += Percentage(
			Font.getbbox("yÓ")[3], 112
		) + 5
	Image_Base.paste(
		Expanded_Images[IMG],
		(
			(Image_Base.size[0] - Expanded_Images[IMG].size[0]) // 2,
			__Y
		),
		Expanded_Images[IMG]
	)
	
# Caption Field Setup

Image_Base = Image_Base.crop(Image_Base.getbbox())

Pasted = Image.new(
	"RGBA",
	(
		int(Config["Media"]["Image"]["Max_Width"]),
		Image_Base.size[1] + Percentage(
			Font.getbbox("yÓ")[3], 150
		)
	),
	__Pasted_Color
)
Pasted.paste(
	Image_Base,
	(
		(Pasted.size[0] - Image_Base.size[0]) // 2,
		(Pasted.size[1] - Image_Base.size[1]) // 2 + ((Font.getsize("yÓ")[1] - Font.getsize("Ó")[1]) if list("qypgj") in Text[:-1] else 0)
	),
	Image_Base
)

if Config["Media"]["Image"]["Watermark"]:
	WM_Size = Config["Media"]["Image"]["Max_Width"] // 55
	WM_Offset = WM_Size // 5
	
	Watermark = Image.open(os.path.join(__BaseDir, "Documents/Pictures/Icons/iFunny.png")).convert("RGBA")
	Watermark = Watermark.resize(
		(WM_Size,) * 2, 1
	)

	Pasted.paste(
		Watermark,
		(
			Pasted.size[0] - Watermark.size[0] - WM_Offset,
			Pasted.size[1] - Watermark.size[1] - WM_Offset
		),
		Watermark
	)
