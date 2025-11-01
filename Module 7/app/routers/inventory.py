from fastapi import APIRouter, Query
from app.services.inventory_service import InventoryService

router = APIRouter(prefix="/api/inventory", tags=["Инвентарь"])


@router.post("/{product_id}/update")
async def update_stock(product_id: int, delta: int = Query(..., description="Change in stock")):
    await InventoryService.update_inventory(product_id, delta)
    return {"message": "Инвентарь обновлен"}
