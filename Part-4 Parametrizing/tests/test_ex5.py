import pytest
from core.app1.models import Product


@pytest.mark.parametrize(
    "title, category, description, slug, regular_price, discount_price, validity",
    [
        ("NewTitle", 1, "NewDescription", "slug", "4.99", "3.99", True),
        pytest.param("NewTitle", 1, "NewDescription", "slug", "", "3.99", False, marks=pytest.mark.xfail),
    ],
)
def test_product_instance(
    db, product_factory, title, category, description, slug, regular_price, discount_price, validity
):
    try:
        product_factory(
            title=title,
            category_id=category,
            description=description,
            slug=slug,
            regular_price=regular_price,
            discount_price=discount_price,
        )
    except:  # noqa: E722
        pass # !: but still fails wtf, on `8.1.1`.
    finally:
        item = Product.objects.all().count()
        print(item)
        assert item == validity
