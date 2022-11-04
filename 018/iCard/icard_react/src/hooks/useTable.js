import { useState } from "react";
import {
  getTablesApi,
  addTablesApi,
  updateTablesApi,
  deleteTablesApi,
} from "../api/table";
import { useAuth } from "./";

export function useTable() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [tables, setTables] = useState(null);

  const { auth } = useAuth();

  const getTables = async () => {
    try {
      setLoading(true);
      const response = await getTablesApi(auth.token);
      setLoading(false);
      setTables(response);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  const addTables = async (data) => {
    try {
      setLoading(true);
      await addTablesApi(data, auth.token);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  const updateTables = async (id, data) => {
    try {
      setLoading(true);
      await updateTablesApi(id, data, auth.token);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  const deleteTables = async (id) => {
    try {
      setLoading(true);
      await deleteTablesApi(id, auth.token);
      setLoading(false);
    } catch (error) {
      setLoading(false);
      setError(error);
    }
  };

  return {
    loading,
    error,
    tables,
    getTables,
    addTables,
    updateTables,
    deleteTables,
  };
}
