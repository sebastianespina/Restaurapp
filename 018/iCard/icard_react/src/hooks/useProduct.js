import { useState } from "react";
import {
  getProductsApi,
  addProductsApi,
  updateProductsApi,
  deleteProductsApi,
} from "../api/product";
import { useAuth } from "./";

export function useProduct() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [products, setProducts] = useState(null);
  const { auth } = useAuth();

  const getProducts = async () => {
    try {
      setLoading(true);
      const response = await getProductsApi();
      setLoading(false);
      setProducts(response);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  const addProduct = async (data) => {
    try {
      setLoading(true);
      await addProductsApi(data, auth.token);
      setLoading(false);
    } catch (error) {
      setError(error);
      setLoading(false);
    }
  };

  const updateProduct = async (id, data) => {
    try {
      setLoading(true);
      await updateProductsApi(id, data, auth.token);
      setLoading(false);
    } catch (error) {
      setError(error);
      setLoading(false);
    }
  };

  const deleteProduct = async (id) => {
    try {
      setLoading(true);
      await deleteProductsApi(id, auth.token);
      setLoading(false);
    } catch (error) {
      setError(error);
      setLoading(false);
    }
  };

  return {
    loading,
    error,
    products,
    getProducts,
    addProduct,
    updateProduct,
    deleteProduct,
  };
}
