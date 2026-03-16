from shiny.playwright import controller
from shiny.run import ShinyAppProc
from playwright.sync_api import Page
from shiny.pytest import create_app_fixture

app = create_app_fixture("../src/app.py")

def test_initial_value_boxes(page: Page, app: ShinyAppProc) -> None:
    """
    Test for checking all two value boxes show correct stats for the full data set.
    """

    page.goto(app.url)

    total_res = controller.ValueBox(page, "total_res")
    avg_rating = controller.ValueBox(page, "avg_rating")
    total_res.expect_value("2826")
    avg_rating.expect_value("4.5")

def test_dataframe_initial(page: Page, app: ShinyAppProc) -> None:
    """
    Test for checking dataframe has the correct columns, number of rows, and
    spot-check a known cell value in the table.
    """
    page.goto(app.url)

    df = controller.OutputDataFrame(page, "tbl_restaurants")
    df.expect_ncol(7)
    df.expect_column_labels(
        ["Restaurant", "Stars", "# of Reviews", "city", 
         "price_range", "category_1", "category_2"]
    )
    df.expect_nrow(2826)
    df.expect_cell("Hankki Korean Street food", row=2, col=0)
    df.expect_cell("4.8", row=2, col=1)


def test_basic_filters(page: Page, app: ShinyAppProc) -> None:
    """ 
    Test for basic filters in the app to ensure filters in the sidebar works as expected. 
    """
    page.goto(app.url)

    # Controllers
    select_price = controller.InputCheckboxGroup(page, "price_range")
    select_cuisine = controller.InputSelect(page, "cuisine")
    
    # Try one filter
    select_price.set(["$$$"])
    select_price.expect_selected(["$$$"])

    # Check value boxes to 17 restaurants with 4.4 average rating
    total_res = controller.ValueBox(page, "total_res")
    avg_rating = controller.ValueBox(page, "avg_rating")

    total_res.expect_value("17")
    avg_rating.expect_value("4.4")

    # Try another filter with multiple selections, expected value 
    # is 7 total restaurants and 4.6 average rating
    select_cuisine.set(["Italian", "Japanese"])
    select_cuisine.expect_selected(["Italian", "Japanese"])
    total_res.expect_value("7")
    avg_rating.expect_value("4.6")

def test_reset_button_restores_default(page: Page, app: ShinyAppProc) -> None:
    """ 
    Test to ensure the reset button returns all values from the original state of the 
    data set. Checking by the value boxes output: Total Restaurant and Average Rating.
    """
    page.goto(app.url)

    total_res = controller.ValueBox(page, "total_res")
    avg_rating = controller.ValueBox(page, "avg_rating")

    select_city = controller.InputSelect(page, "city")
    reset_button = controller.InputActionButton(page, "reset_filters")

    select_city.set(["Brampton", "Edmonton"])
    select_city.expect_selected(["Brampton", "Edmonton"])

    # Check if the filter works
    total_res.expect_value("241")
    avg_rating.expect_value("4.4")

    # Check if the reset button works
    reset_button.click()
    total_res.expect_value("2826")
    avg_rating.expect_value("4.5")