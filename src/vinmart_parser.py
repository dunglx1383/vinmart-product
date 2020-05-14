from dataclasses import dataclass
from typing import Any, List, Optional, TypeVar, Callable, Type, cast
from enum import Enum

from type_validation import from_float, from_int, from_list, to_class, from_union, from_none, from_str, to_enum, from_bool

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


@dataclass
class PriceRange:
    max_price: float
    min_price: float

    @staticmethod
    def from_dict(obj: Any) -> 'PriceRange':
        assert isinstance(obj, dict)
        max_price = from_float(obj.get("maxPrice"))
        min_price = from_float(obj.get("minPrice"))
        return PriceRange(max_price, min_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maxPrice"] = from_int(self.max_price)
        result["minPrice"] = from_int(self.min_price)
        return result


@dataclass
class Extra:
    total_items: int
    page: int
    page_size: int
    price_ranges: List[PriceRange]

    @staticmethod
    def from_dict(obj: Any) -> 'Extra':
        assert isinstance(obj, dict)
        total_items = from_int(obj.get("totalItems"))
        page = from_int(obj.get("page"))
        page_size = from_int(obj.get("pageSize"))
        price_ranges = from_list(PriceRange.from_dict, obj.get("priceRanges"))
        return Extra(total_items, page, page_size, price_ranges)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalItems"] = from_int(self.total_items)
        result["page"] = from_int(self.page)
        result["pageSize"] = from_int(self.page_size)
        result["priceRanges"] = from_list(lambda x: to_class(PriceRange, x), self.price_ranges)
        return result


@dataclass
class AttributeSet:
    id: int
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'AttributeSet':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        return AttributeSet(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = self.name
        return result


@dataclass
class Brand:
    code: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Brand':
        assert isinstance(obj, dict)
        code = from_union([from_none, from_str], obj.get("code"))
        name = from_union([from_none, from_str], obj.get("name"))
        return Brand(code, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_none, from_str], self.code)
        result["name"] = from_union([from_none, from_str], self.name)
        return result


@dataclass
class Category:
    id: int
    code: str
    name: str
    level: int
    parent_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        code = from_str(obj.get("code"))
        name = from_str(obj.get("name"))
        level = from_int(obj.get("level"))
        parent_id = from_int(obj.get("parentId"))
        return Category(id, code, name, level, parent_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["code"] = from_str(self.code)
        result["name"] = from_str(self.name)
        result["level"] = from_int(self.level)
        result["parentId"] = from_int(self.parent_id)
        return result


@dataclass
class Image:
    url: str
    priority: int
    path: str

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        url = from_str(obj.get("url"))
        priority = from_int(obj.get("priority"))
        path = from_str(obj.get("path"))
        return Image(url, priority, path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_str(self.url)
        result["priority"] = from_int(self.priority)
        result["path"] = from_str(self.path)
        return result


@dataclass
class BundleProduct:
    sku: str
    quantity: int
    priority: int
    name: str
    display_name: None
    url: None
    image_url: None

    @staticmethod
    def from_dict(obj: Any) -> 'BundleProduct':
        assert isinstance(obj, dict)
        sku = from_str(obj.get("sku"))
        quantity = from_int(obj.get("quantity"))
        priority = from_int(obj.get("priority"))
        name = from_str(obj.get("name"))
        display_name = from_none(obj.get("displayName"))
        url = from_none(obj.get("url"))
        image_url = from_none(obj.get("imageUrl"))
        return BundleProduct(sku, quantity, priority, name, display_name, url, image_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sku"] = from_str(self.sku)
        result["quantity"] = from_int(self.quantity)
        result["priority"] = from_int(self.priority)
        result["name"] = from_str(self.name)
        result["displayName"] = from_none(self.display_name)
        result["url"] = from_none(self.url)
        result["imageUrl"] = from_none(self.image_url)
        return result


@dataclass
class ParentBundle:
    sku: str
    name: str
    display_name: None

    @staticmethod
    def from_dict(obj: Any) -> 'ParentBundle':
        assert isinstance(obj, dict)
        sku = from_str(obj.get("sku"))
        name = from_str(obj.get("name"))
        display_name = from_none(obj.get("displayName"))
        return ParentBundle(sku, name, display_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sku"] = from_str(self.sku)
        result["name"] = from_str(self.name)
        result["displayName"] = from_none(self.display_name)
        return result


@dataclass
class Price:
    supplier_sale_price: float
    sell_price: float

    @staticmethod
    def from_dict(obj: Any) -> 'Price':
        assert isinstance(obj, dict)
        supplier_sale_price = from_float(obj.get("supplierSalePrice"))
        sell_price = from_float(obj.get("sellPrice"))
        return Price(supplier_sale_price, sell_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["supplierSalePrice"] = from_int(self.supplier_sale_price)
        result["sellPrice"] = from_int(self.sell_price)
        return result


class Channel(Enum):
    VINMART_ONLINE = "vinmart_online"


class Terminal(Enum):
    VMA_OLN_WEB_0003 = "VMA_OLN_WEB_0003"


@dataclass
class PromotionPrice:
    channel: Channel
    terminal: Terminal
    final_price: float
    promotion_price: None
    best_price: float
    flash_sale_price: None

    @staticmethod
    def from_dict(obj: Any) -> 'PromotionPrice':
        assert isinstance(obj, dict)
        channel = Channel(obj.get("channel"))
        terminal = Terminal(obj.get("terminal"))
        final_price = from_float(obj.get("finalPrice"))
        promotion_price = from_none(obj.get("promotionPrice"))
        best_price = from_float(obj.get("bestPrice"))
        flash_sale_price = from_none(obj.get("flashSalePrice"))
        return PromotionPrice(channel, terminal, final_price, promotion_price, best_price, flash_sale_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel"] = to_enum(Channel, self.channel)
        result["terminal"] = to_enum(Terminal, self.terminal)
        result["finalPrice"] = from_int(self.final_price)
        result["promotionPrice"] = from_none(self.promotion_price)
        result["bestPrice"] = from_int(self.best_price)
        result["flashSalePrice"] = from_none(self.flash_sale_price)
        return result


@dataclass
class Rating:
    average_point: None
    vote_count: int

    @staticmethod
    def from_dict(obj: Any) -> 'Rating':
        assert isinstance(obj, dict)
        average_point = from_none(obj.get("averagePoint"))
        vote_count = from_int(obj.get("voteCount"))
        return Rating(average_point, vote_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["averagePoint"] = from_none(self.average_point)
        result["voteCount"] = from_int(self.vote_count)
        return result


class DisplayName(Enum):
    BLUE = "Blue"


class SellerName(Enum):
    CÔNG_TY_CÔ_PHẦN_DỊCH_VỤ_THƯƠNG_MẠI_TỔNG_HỢP_VINCOMMERCE = "Công Ty Cô Phần Dịch Vụ Thương Mại Tổng Hợp Vincommerce"


@dataclass
class Seller:
    id: int
    name: SellerName
    display_name: DisplayName

    @staticmethod
    def from_dict(obj: Any) -> 'Seller':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = SellerName(obj.get("name"))
        display_name = DisplayName(obj.get("displayName"))
        return Seller(id, name, display_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = to_enum(SellerName, self.name)
        result["displayName"] = to_enum(DisplayName, self.display_name)
        return result


@dataclass
class SEOInfo:
    meta_keyword: None
    meta_title: None
    meta_description: None
    short_description: str
    description: None

    @staticmethod
    def from_dict(obj: Any) -> 'SEOInfo':
        assert isinstance(obj, dict)
        meta_keyword = from_none(obj.get("metaKeyword"))
        meta_title = from_none(obj.get("metaTitle"))
        meta_description = from_none(obj.get("metaDescription"))
        short_description = from_str(obj.get("shortDescription"))
        description = from_none(obj.get("description"))
        return SEOInfo(meta_keyword, meta_title, meta_description, short_description, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["metaKeyword"] = from_none(self.meta_keyword)
        result["metaTitle"] = from_none(self.meta_title)
        result["metaDescription"] = from_none(self.meta_description)
        result["shortDescription"] = from_str(self.short_description)
        result["description"] = from_none(self.description)
        return result


class Sale(Enum):
    HANG_BAN = "hang_ban"


@dataclass
class Status:
    publish: bool
    need_manage_stock: bool
    sale: Sale

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        assert isinstance(obj, dict)
        publish = from_bool(obj.get("publish"))
        need_manage_stock = from_bool(obj.get("needManageStock"))
        sale = Sale(obj.get("sale"))
        return Status(publish, need_manage_stock, sale)

    def to_dict(self) -> dict:
        result: dict = {}
        result["publish"] = from_bool(self.publish)
        result["needManageStock"] = from_bool(self.need_manage_stock)
        result["sale"] = to_enum(Sale, self.sale)
        return result


class TypeEnum(Enum):
    BIZ = "Biz"


@dataclass
class TotalAvailableByStock:
    type: TypeEnum
    total: float

    @staticmethod
    def from_dict(obj: Any) -> 'TotalAvailableByStock':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        total = float(obj.get("total"))
        return TotalAvailableByStock(type, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
        result["total"] = from_int(self.total)
        return result


class Code(Enum):
    VIN_ETON_HCM = "VIN-ETON-HCM"


@dataclass
class TotalAvailableByStore:
    code: Code
    total: float

    @staticmethod
    def from_dict(obj: Any) -> 'TotalAvailableByStore':
        assert isinstance(obj, dict)
        code = Code(obj.get("code"))
        total = from_float(obj.get("total"))
        return TotalAvailableByStore(code, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = to_enum(Code, self.code)
        result["total"] = from_int(self.total)
        return result


@dataclass
class Product:
    sku: str
    name: str
    url: str
    seller: Seller
    brand: Brand
    status: Status
    objective: Brand
    product_type: Brand
    images: List[Image]
    price: Price
    product_line: Brand
    stocks: List[Any]
    total_available_by_stores: List[TotalAvailableByStore]
    total_available: float
    is_bundle: bool
    bundle_products: None
    parent_bundles: None
    total_available_by_stocks: List[TotalAvailableByStock]
    serial_generated: bool
    serial_managed: bool
    display_name: str
    color: Brand
    tags: List[Any]
    promotion_prices: List[PromotionPrice]
    promotions: List[Any]
    flash_sales: List[Any]
    attribute_set: AttributeSet
    categories: List[Category]
    seller_categories: List[Category]
    magento_id: int
    seo_info: SEOInfo
    rating: Rating
    all_active_flash_sales: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'Product':
        assert isinstance(obj, dict)
        sku = from_str(obj.get("sku"))
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        seller = Seller.from_dict(obj.get("seller"))
        brand = Brand.from_dict(obj.get("brand"))
        status = Status.from_dict(obj.get("status"))
        objective = Brand.from_dict(obj.get("objective"))
        product_type = Brand.from_dict(obj.get("productType"))
        images = from_list(Image.from_dict, obj.get("images"))
        price = Price.from_dict(obj.get("price"))
        product_line = Brand.from_dict(obj.get("productLine"))
        stocks = from_list(lambda x: x, obj.get("stocks"))
        total_available_by_stores = from_list(TotalAvailableByStore.from_dict, obj.get("totalAvailableByStores"))
        total_available = from_float(obj.get("totalAvailable"))
        is_bundle = from_bool(obj.get("isBundle"))
        bundle_products = from_union([from_none, lambda x: from_list(BundleProduct.from_dict, x)], obj.get("bundleProducts"))
        parent_bundles = from_union([lambda x: from_list(ParentBundle.from_dict, x), from_none], obj.get("parentBundles"))
        total_available_by_stocks = from_list(TotalAvailableByStock.from_dict, obj.get("totalAvailableByStocks"))
        serial_generated = from_bool(obj.get("serialGenerated"))
        serial_managed = from_bool(obj.get("serialManaged"))
        display_name = from_str(obj.get("displayName"))
        color = Brand.from_dict(obj.get("color"))
        tags = from_list(lambda x: x, obj.get("tags"))
        promotion_prices = from_list(PromotionPrice.from_dict, obj.get("promotionPrices"))
        promotions = from_list(lambda x: x, obj.get("promotions"))
        flash_sales = from_list(lambda x: x, obj.get("flashSales"))
        attribute_set = AttributeSet.from_dict(obj.get("attributeSet"))
        categories = from_list(Category.from_dict, obj.get("categories"))
        seller_categories = from_list(Category.from_dict, obj.get("sellerCategories"))
        magento_id = from_int(obj.get("magentoId"))
        seo_info = SEOInfo.from_dict(obj.get("seoInfo"))
        rating = Rating.from_dict(obj.get("rating"))
        all_active_flash_sales = from_list(lambda x: x, obj.get("allActiveFlashSales"))
        return Product(sku, name, url, seller, brand, status, objective, product_type, images, price, product_line, stocks, total_available_by_stores, total_available, is_bundle, bundle_products, parent_bundles, total_available_by_stocks, serial_generated, serial_managed, display_name, color, tags, promotion_prices, promotions, flash_sales, attribute_set, categories, seller_categories, magento_id, seo_info, rating, all_active_flash_sales)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sku"] = from_str(self.sku)
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        result["seller"] = to_class(Seller, self.seller)
        result["brand"] = to_class(Brand, self.brand)
        result["status"] = to_class(Status, self.status)
        result["objective"] = to_class(Brand, self.objective)
        result["productType"] = to_class(Brand, self.product_type)
        result["images"] = from_list(lambda x: to_class(Image, x), self.images)
        result["price"] = to_class(Price, self.price)
        result["productLine"] = to_class(Brand, self.product_line)
        result["stocks"] = from_list(lambda x: x, self.stocks)
        result["totalAvailableByStores"] = from_list(lambda x: to_class(TotalAvailableByStore, x), self.total_available_by_stores)
        result["totalAvailable"] = from_int(self.total_available)
        result["isBundle"] = from_bool(self.is_bundle)
        result["bundleProducts"] = from_union([from_none, lambda x: from_list(lambda x: to_class(BundleProduct, x), x)], self.bundle_products)
        result["parentBundles"] = from_union([lambda x: from_list(lambda x: to_class(ParentBundle, x), x), from_none], self.parent_bundles)
        result["totalAvailableByStocks"] = from_list(lambda x: to_class(TotalAvailableByStock, x), self.total_available_by_stocks)
        result["serialGenerated"] = from_bool(self.serial_generated)
        result["serialManaged"] = from_bool(self.serial_managed)
        result["displayName"] = from_str(self.display_name)
        result["color"] = to_class(Brand, self.color)
        result["tags"] = from_list(lambda x: x, self.tags)
        result["promotionPrices"] = from_list(lambda x: to_class(PromotionPrice, x), self.promotion_prices)
        result["promotions"] = from_list(lambda x: x, self.promotions)
        result["flashSales"] = from_list(lambda x: x, self.flash_sales)
        result["attributeSet"] = to_class(AttributeSet, self.attribute_set)
        result["categories"] = from_list(lambda x: to_class(Category, x), self.categories)
        result["sellerCategories"] = from_list(lambda x: to_class(Category, x), self.seller_categories)
        result["magentoId"] = from_int(self.magento_id)
        result["seoInfo"] = to_class(SEOInfo, self.seo_info)
        result["rating"] = to_class(Rating, self.rating)
        result["allActiveFlashSales"] = from_list(lambda x: x, self.all_active_flash_sales)
        return result


@dataclass
class Result:
    products: List[Product]
    keywords: List[Any]
    filters: List[Any]

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        assert isinstance(obj, dict)
        products = from_list(Product.from_dict, obj.get("products"))
        keywords = from_list(lambda x: x, obj.get("keywords"))
        filters = from_list(lambda x: x, obj.get("filters"))
        return Result(products, keywords, filters)

    def to_dict(self) -> dict:
        result: dict = {}
        result["products"] = from_list(lambda x: to_class(Product, x), self.products)
        result["keywords"] = from_list(lambda x: x, self.keywords)
        result["filters"] = from_list(lambda x: x, self.filters)
        return result


@dataclass
class VinmartProduct:
    code: str
    result: Result
    extra: Extra

    @staticmethod
    def from_dict(obj: Any) -> 'VinmartProduct':
        assert isinstance(obj, dict)
        code = from_str(obj.get("code"))
        result = Result.from_dict(obj.get("result"))
        extra = Extra.from_dict(obj.get("extra"))
        return VinmartProduct(code, result, extra)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_str(self.code)
        result["result"] = to_class(Result, self.result)
        result["extra"] = to_class(Extra, self.extra)
        return result


def vinmart_product_from_dict(s: Any) -> VinmartProduct:
    return VinmartProduct.from_dict(s)


def vinmart_product_to_dict(x: VinmartProduct) -> Any:
    return to_class(VinmartProduct, x)
