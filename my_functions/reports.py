import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px
# from simple_term_menu import TerminalMenu


def full_table(my_wardrobe):
    list_items = my_wardrobe.list_items()

    cells = [list(item.__dict__.values()) for item in list_items]
    cells.insert(0, list(list_items[0].__dict__.keys()))  # header

    fig = ff.create_table(cells, index=True)

    # fig.update_layout(
    #     title_text='2016 Hockey Stats',
    #     margin={'t': 50, 'b': 100},
    #     # xaxis={'domain': [0, .5]},
    #     # xaxis2={'domain': [0.6, 1.]},
    #     # yaxis2={'anchor': 'x2', 'title': 'Goals'}
    # )
    fig.show()


def bar_prices(my_wardrobe):
    list_items = my_wardrobe.list_items()


