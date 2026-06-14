import { useState, ChangeEvent } from "react"
import type { ProductType } from "../types/ProductType"

function ProductForm() {

  const [product, setProduct] = useState<ProductType>({
    title: "",
    count: 0,
    price: 0,
    is_active: false
  })

  function changeTitle(e: ChangeEvent<HTMLInputElement>) {
    setProduct({
      ...product,
      title: e.target.value
    })
  }

  function changeCount(e: ChangeEvent<HTMLInputElement>) {
    setProduct({
      ...product,
      count: +e.target.value
    })
  }

  function changePrice(e: ChangeEvent<HTMLInputElement>) {
    setProduct({
      ...product,
      price: +e.target.value
    })
  }

  function changeActive(e: ChangeEvent<HTMLInputElement>) {
    setProduct({
      ...product,
      is_active: e.target.checked
    })
  }

  return (
    <div>

      <h2>Product</h2>

      <p>
        <strong>Title:</strong> {product.title} <br />
        <strong>Count:</strong> {product.count} <br />
        <strong>Price:</strong> {product.price} <br />
        <strong>Status:</strong>{" "}
        {product.is_active ? "Active" : "Non active"}
      </p>

      <hr />

      {/* Title */}
      <label>
        Title:
        <input
          type="text"
          value={product.title}
          onChange={changeTitle}
        />
      </label>

      <br /><br />

      {/* Count */}
      <label>
        Count:
        <input
          type="number"
          value={product.count}
          onChange={changeCount}
        />
      </label>

      <br /><br />

      {/* Price */}
      <label>
        Price:
        <input
          type="number"
          value={product.price}
          onChange={changePrice}
        />
      </label>

      <br /><br />

      {/* Checkbox */}
      <label>
        Active:
        <input
          type="checkbox"
          checked={product.is_active}
          onChange={changeActive}
        />
      </label>

    </div>
  )
}

export default ProductForm