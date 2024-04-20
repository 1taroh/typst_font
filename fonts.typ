== フォント
#let text_example = "Hello World! 木曾路はすべて山の中である。"
#for entry in json("fonts.json").at("entries") {
  text(
    font:entry.name,
    [- #entry.name : #text_example]
    )
}