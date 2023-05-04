from overlord_manager import OverlordManager
from config import ConfigManager
from data import DataManager
from strategies import StrategyManager
from backtesting import BacktestManager
from trading import TradingManager
from risk_management import RiskManagementManager
from report import ReportManager

if __name__ == "__main__":
    config_manager = ConfigManager()
    data_manager = DataManager(config_manager)
    strategy_manager = StrategyManager(config_manager)
    backtest_manager = BacktestManager(config_manager)
    trading_manager = TradingManager(config_manager)
    risk_management_manager = RiskManagementManager(config_manager)
    report_manager = ReportManager(config_manager)

    overlord_manager = OverlordManager(data_manager, strategy_manager, backtest_manager, trading_manager, risk_management_manager, report_manager)
    overlord_manager.start()
